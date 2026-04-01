#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re

# Add lib directory to path
lib_path = os.path.join(os.path.dirname(__file__), 'lib')
sys.path.insert(0, lib_path)

import xbmc
import xbmcgui
from github_fetcher import GitHubSubtitleFetcher
from subtitle_matcher import SubtitleMatcher

class SabriMaryananSubtitleService:
    def __init__(self):
        self.fetcher = GitHubSubtitleFetcher(
            repo_url="https://github.com/motekamazon-droid/sabri-maranan-subtitles",
            base_path="en/s01"
        )
        self.matcher = SubtitleMatcher()
        self.log("Sabri Maranan Subtitles Service started")

    def log(self, msg):
        xbmc.log(f"[Sabri Maranan Subtitles] {msg}", xbmc.LOGINFO)

    def log_error(self, msg):
        xbmc.log(f"[Sabri Maranan Subtitles] ERROR: {msg}", xbmc.LOGERROR)

    def on_playback_started(self):
        """Called when playback starts"""
        try:
            # Get current playing file
            player = xbmc.Player()
            if not player.isPlaying():
                return

            filename = player.getPlayingFile()
            if not filename:
                return

            # Extract episode number from filename
            ep_num = self.matcher.extract_episode_number(filename)
            if not ep_num:
                self.log(f"Could not extract episode number from: {filename}")
                return

            self.log(f"Detected episode: {ep_num}")

            # Fetch subtitle from GitHub
            srt_filename = self.matcher.get_subtitle_filename(ep_num)
            subtitle_path = self.fetcher.fetch_subtitle(ep_num, srt_filename)

            if subtitle_path:
                # Add subtitle to player
                player.setSubtitles(subtitle_path)
                self.log(f"✓ Loaded subtitle: {srt_filename}")
            else:
                self.log(f"⚠ Subtitle not found for episode {ep_num}")

        except Exception as e:
            self.log_error(f"Exception in on_playback_started: {str(e)}")

    def run(self):
        """Main service loop"""
        self.log("Service monitoring playback...")
        monitor = xbmc.Monitor()

        while not monitor.abortRequested():
            try:
                # Check if something is playing
                player = xbmc.Player()
                if player.isPlaying():
                    # Get filename
                    filename = player.getPlayingFile()

                    # Check if it's a Sabri Maranan file (case insensitive)
                    if 'sabri' in filename.lower() or 'maranan' in filename.lower():
                        # Try to add subtitle
                        self.on_playback_started()

                # Small wait to reduce CPU usage
                if monitor.waitForAbort(2):  # Wait 2 seconds or until abort
                    break

            except Exception as e:
                self.log_error(f"Exception in run loop: {str(e)}")
                if monitor.waitForAbort(5):
                    break

if __name__ == '__main__':
    service = SabriMaryananSubtitleService()
    service.run()
