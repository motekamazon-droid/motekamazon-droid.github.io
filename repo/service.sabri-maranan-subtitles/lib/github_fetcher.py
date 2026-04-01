#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile
import urllib.request
import urllib.error

class GitHubSubtitleFetcher:
    """Fetch subtitles from GitHub public repository"""

    def __init__(self, repo_url, base_path):
        """
        Initialize fetcher

        Args:
            repo_url: GitHub repo URL (e.g., https://github.com/user/repo)
            base_path: Path within repo (e.g., en/s01)
        """
        self.repo_url = repo_url.rstrip('/')
        self.base_path = base_path.strip('/')

        # Convert to raw GitHub URL
        # https://github.com/user/repo -> https://raw.githubusercontent.com/user/repo/main
        parts = self.repo_url.replace('https://', '').replace('http://', '').split('/')
        if len(parts) >= 2:
            self.raw_base = f"https://raw.githubusercontent.com/{parts[1]}/{parts[2]}/main"
        else:
            self.raw_base = self.repo_url

    def fetch_subtitle(self, episode_num, filename):
        """
        Fetch subtitle file from GitHub and save locally

        Args:
            episode_num: Episode number (e.g., 1, 12, 42)
            filename: SRT filename (e.g., sabri_maranan_s1e01_english-Title.srt)

        Returns:
            Path to downloaded subtitle, or None if not found
        """
        try:
            # Construct raw GitHub URL
            url = f"{self.raw_base}/{self.base_path}/{filename}"

            # Create temp directory for subtitles
            temp_dir = os.path.join(tempfile.gettempdir(), 'kodi_subtitles')
            os.makedirs(temp_dir, exist_ok=True)

            # Download file
            local_path = os.path.join(temp_dir, filename)

            # Skip if already cached
            if os.path.exists(local_path):
                return local_path

            # Fetch from GitHub (no auth needed for public repos)
            urllib.request.urlretrieve(url, local_path)

            return local_path

        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None  # File not found
            raise
        except Exception as e:
            print(f"Error fetching subtitle: {str(e)}")
            return None

    def get_raw_url(self, filename):
        """Get the raw GitHub URL for a file"""
        return f"{self.raw_base}/{self.base_path}/{filename}"
