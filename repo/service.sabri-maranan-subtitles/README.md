# Sabri Maranan Subtitles Kodi Addon

Automatically fetches and applies English subtitles for Sabri Maranan episodes from GitHub when playing videos in Kodi.

## Features

- **Auto-detection**: Detects Sabri Maranan episodes by filename
- **Episode matching**: Extracts episode number from filename (supports s1e12, S01E12, etc.)
- **GitHub integration**: Fetches subtitles from public GitHub repo (no login needed)
- **Caching**: Caches downloaded subtitles for faster playback
- **Silent operation**: No popups or user interaction required

## Installation

1. Download the addon folder: `service.sabri-maranan-subtitles`
2. Create a ZIP file of the addon folder
3. In Kodi:
   - Settings → Add-ons → Install from zip file
   - Select the zip file
4. Enable the addon in Settings → Add-ons → Services
5. The service will start automatically

## Usage

Simply play a Sabri Maranan episode. The addon will:
1. Detect the episode number from the filename
2. Fetch the matching subtitle from GitHub
3. Automatically load the subtitle
4. Display the subtitle while playing

## Supported Episodes

Episodes 1-15 currently have English subtitles. New episodes are added as they are processed.

## Episode Number Patterns Supported

The addon recognizes the following filename patterns:
- `sabri_maranan_s1e12` (default Kodi pattern)
- `S01E12`, `s1e12`, `S1E12`
- `Episode 12`, `Ep12`, `E12`
- `Season 1 Episode 12`

## How It Works

1. **Filename Detection**: When a video starts playing, the addon checks if it's a Sabri Maranan episode
2. **Episode Extraction**: Extracts the episode number from the filename
3. **Subtitle Download**: Fetches the matching subtitle from GitHub:
   - URL: `https://raw.githubusercontent.com/motekamazon-droid/sabri-maranan-subtitles/main/en/s01/{filename}.srt`
4. **Subtitle Application**: Applies the subtitle to the current playback
5. **Caching**: Stores downloaded files temporarily for quick subsequent plays

## Subtitle Source

Repository: https://github.com/motekamazon-droid/sabri-maranan-subtitles

## Requirements

- Kodi 20+ (Matrix/Nexus) with Python 3.11+
- Internet connection to fetch subtitles from GitHub

## Troubleshooting

### Subtitles not loading
- Check that your internet connection is working
- Verify episode number is in the filename (e.g., e12, s1e12)
- Check Kodi logs for error messages: Settings → System → Logging → Enable component specific logging

### Missing subtitles for certain episodes
- If no subtitle is found, the addon silently continues playback
- Check the GitHub repo to see which episodes are available

## License

GPL-2.0

## Source

https://github.com/motekamazon-droid/sabri-maranan-subtitles
