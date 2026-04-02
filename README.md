# Sabri Maranan Subtitles Repository

English subtitles for the Israeli comedy series **"Sabri Maranan"** (סברי מרנן).

Automatic subtitle fetching addon for **Kodi** media center.

---

## 🎬 Quick Start

### Download Repository Addon ZIP
```
https://raw.githubusercontent.com/motekamazon-droid/repo/main/zips/repository.sabri-maranan/repository.sabri-maranan-1.0.0.zip
```

### Installation
1. In Kodi: **Settings** → **Add-ons** → **Install from ZIP file**
2. Select the downloaded ZIP
3. Then install **Sabri Maranan Subtitles** from the repository

### Usage
Play any Sabri Maranan episode - subtitles load automatically!

---

## ✨ Features

- ✅ **Automatic subtitles** - No manual downloads or configuration
- ✅ **All episodes** - Episodes 1-17 supported
- ✅ **Auto-detection** - Works with any episode filename format
- ✅ **No login** - Public GitHub repository
- ✅ **Caching** - Fast repeat playback
- ✅ **Silent** - No popups or notifications

---

## 📊 Progress

- **17/42** episodes completed with English subtitles
- Automatically updated as new episodes are processed
- Last updated: April 2, 2026

---

## 📁 Repository Structure

```
repo/
├── addons.xml                    (Master addon list)
├── addons.xml.md5               (Checksum)
├── repository.sabri-maranan/    (Repository addon source)
│   ├── addon.xml
│   ├── icon.png
│   └── fanart.jpg
├── zips/                        (Packaged addons)
│   ├── repository.sabri-maranan/
│   │   ├── repository.sabri-maranan-1.0.0.zip
│   │   └── repository.sabri-maranan-1.0.0.zip.md5
│   └── service.sabri-maranan-subtitles/
│       ├── service.sabri-maranan-subtitles-1.0.0.zip
│       └── service.sabri-maranan-subtitles-1.0.0.zip.md5
└── en/s01/                      (Subtitle files)
    ├── sabri_maranan_s1e01_english-*.srt
    ├── sabri_maranan_s1e02_english-*.srt
    └── ... (17 episodes)
```

---

## 🔗 Links

- **GitHub Repository**: https://github.com/motekamazon-droid/repo
- **Repository Addon ZIP**: https://raw.githubusercontent.com/motekamazon-droid/repo/main/zips/repository.sabri-maranan/repository.sabri-maranan-1.0.0.zip
- **Installation Guide**: See [KODI_INSTALL.md](KODI_INSTALL.md)

---

## 📝 Subtitle Files

All English subtitles are organized by season and episode:

**Location:** `/en/s01/`

**Format:** `sabri_maranan_s1eXX_english-{episode_name}.srt`

**Episodes Available:** 1-17 (Season 1)

---

## 🤖 Automated Updates

New episodes are processed and added to the repository automatically:
- Daily processing at midnight (UTC)
- 2 episodes processed per day
- Automatically synced to GitHub
- Available immediately in Kodi addon

---

## 📋 Subtitle Quality

Each subtitle file has been:
- ✅ Extracted from video
- ✅ OCR processed
- ✅ Manually reviewed
- ✅ Spell-checked
- ✅ Timing adjusted for accuracy

---

## 🛠️ Technical Details

**Kodi Addon:** `service.sabri-maranan-subtitles`
**Type:** Service addon (background subtitle fetching)
**Python Version:** 3.0.0+
**License:** GPL-2.0

**How it works:**
1. Monitors video playback in Kodi
2. Detects Sabri Maranan episodes by filename
3. Fetches matching English subtitles from GitHub
4. Auto-applies subtitles to the video
5. Caches subtitles for fast repeat access

---

## 💬 Support

For issues or questions:
- Check [KODI_INSTALL.md](KODI_INSTALL.md) Troubleshooting section
- Review Kodi debug logs (Settings → System → Logging)
- Visit GitHub repository: https://github.com/motekamazon-droid/repo

---

**Repository Owner:** motekamazon-droid  
**Last Updated:** April 2, 2026
