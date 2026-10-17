#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
ui_root = root / "app/src/main/java/com/abn3li/telemusic/ui"

# Only replace exact quoted UI text. Avoid broad token replacement so routes/API values stay intact.
common = {
    "Get Started": "开始使用",
    "Continue": "继续",
    "Back": "返回",
    "Cancel": "取消",
    "Done": "完成",
    "Close": "关闭",
    "Save": "保存",
    "Delete": "删除",
    "Remove": "移除",
    "Change": "更改",
    "Choose": "选择",
    "Choose Folder…": "选择文件夹…",
    "Decide later": "稍后决定",
    "Start Listening": "开始聆听",
    "Sign In": "登录",
    "Sign Out": "退出登录",
    "Change Account": "切换账号",
    "Connected": "已连接",
    "Settings": "设置",
    "Home": "主页",
    "Discover": "发现",
    "Search": "搜索",
    "Library": "资料库",
    "Playlists": "播放列表",
    "Artists": "艺人",
    "Albums": "专辑",
    "Songs": "歌曲",
    "Downloads": "下载",
    "Local music": "本地音乐",
    "Pinned": "已置顶",
    "Recently added": "最近添加",
    "Recently Added": "最近添加",
    "Recently Played": "最近播放",
    "Top Artists": "热门艺人",
    "Made for You": "为你推荐",
    "New releases": "新发行",
    "New Releases": "新发行",
    "Liked": "喜欢",
    "Downloaded": "已下载",
    "Shuffle": "随机播放",
    "Daily Mix": "每日混合",
    "Your most played": "你最常播放的歌曲",
    "Rediscover": "重新发现",
    "Not played in a while": "好久没听的歌曲",
    "See All": "查看全部",
    "See all": "查看全部",
    "Play all": "全部播放",
    "Create playlist": "新建播放列表",
    "Playing next": "接下来播放",
    "Playing Next": "接下来播放",
    "Play Next": "下一首播放",
    "Add to Queue": "加入队列",
    "Add to Playlist": "加入播放列表",
    "Go to Artist": "前往艺人",
    "Go to Album": "前往专辑",
    "Song Info": "歌曲信息",
    "Lyrics": "歌词",
    "Pause": "暂停",
    "Play": "播放",
    "Next": "下一首",
    "Previous": "上一首",
    "Download": "下载",
    "Downloading…": "正在下载…",
    "Remove Download": "删除下载",
    "You might also like": "你可能也喜欢",
    "Import from Folder": "从文件夹导入",
    "Remove Account": "移除账号",
    "Audio Quality": "音频质量",
    "Now Playing": "正在播放",
    "Accounts": "账号",
    "Home Feeds": "主页内容",
    "Appearance": "外观",
    "Lyrics Glow": "歌词辉光",
    "Lyrics Blur": "歌词模糊",
    "Animated Background": "动态背景",
    "Auto-fetch Song Info": "自动获取歌曲信息",
    "Import Local Songs": "导入本地歌曲",
    "Download Location": "下载位置",
    "App Storage": "应用存储",
    "Clear Cache": "清除缓存",
    "Clear Library": "清空资料库",
    "About": "关于",
    "Check for Updates": "检查更新",
    "Open-source Licenses": "开源许可",
    "Licenses": "许可",
    "Sync": "同步",
    "Importing from Spotify": "正在从 Spotify 导入",
    "Browse Categories": "浏览分类",
    "Your Imported Playlists": "你导入的播放列表",
    "Import playlist": "导入播放列表",
    "Playing next": "下一首播放",
    "No results": "没有结果",
    "Try again": "重试",
    "Retry": "重试",
    "Loading…": "加载中…",
    "Unknown title": "未知标题",
    "Unknown artist": "未知艺人",
}

phrases = {
    "Telegram needs a quick setup. You can do it any time in Settings > Telegram.": "Telegram 需要简单设置，你可以随时前往“设置 > Telegram”完成。",
    "Welcome to TeleMusic": "欢迎使用 TeleMusic",
    "Your music from Telegram, YouTube and Spotify, together in one player.": "将 Telegram、YouTube 和 Spotify 的音乐汇聚在一个播放器中。",
    "Play songs from your channels and chats": "播放频道和聊天中的歌曲",
    "Stream or download any song": "在线播放或下载歌曲",
    "Bring your playlists and Liked Songs": "导入播放列表和已点赞歌曲",
    "On this phone": "这台手机",
    "Add your own music files": "添加你自己的音乐文件",
    "Everything in one player": "一个播放器，全部搞定",
    "Made to feel good every time you press play.": "每一次播放，都自然顺手。",
    "Synced lyrics": "同步歌词",
    "Sing along, line by line": "逐行同步，跟着一起唱",
    "Play offline": "离线播放",
    "Download songs and whole playlists": "下载歌曲或整个播放列表",
    "Daily mixes from what you play": "根据你的播放习惯生成每日混合",
    "In the car": "车载播放",
    "Android Auto, Bluetooth and lock screen": "支持 Android Auto、蓝牙和锁屏控制",
    "Control music from your home screen": "直接从主屏幕控制音乐",
    "Private": "隐私保护",
    "No sign-up. Your music stays on your phone": "无需注册，音乐留在你的设备上",
    "Notifications are on": "通知已开启",
    "Allow Notifications": "允许通知",
    "Not now": "暂不",
    "Turn on notifications": "开启通知",
    "See what's playing, control your music from the lock screen, and follow downloads, Telegram syncs and Spotify imports.": "查看正在播放的内容、在锁屏控制音乐，并跟踪下载、Telegram 同步和 Spotify 导入进度。",
    "Where should downloads go?": "下载内容保存到哪里？",
    "Songs you download play without internet. You can change this later in Settings.": "下载后的歌曲可离线播放，之后也能在设置中修改。",
    "A folder on your phone": "手机中的文件夹",
    "Your file manager and other music apps can see the songs": "文件管理器和其他音乐应用都能看到这些歌曲",
    "No folder chosen yet": "尚未选择文件夹",
    "Inside TeleMusic": "TeleMusic 内部",
    "Private to the app, removed if you uninstall it": "仅供应用使用，卸载应用时会一并删除",
    "No storage permission needed: TeleMusic can only use the folder you pick.": "无需存储权限：TeleMusic 只能访问你选择的文件夹。",
    "Home feeds are turned off. Enable them in Settings.": "主页内容已关闭，请在设置中开启。",
    "Loading feed": "正在加载主页内容",
    "Songs you add to your library appear here.": "添加到资料库的歌曲会显示在这里。",
    "Telegram Feed": "Telegram 内容",
    "Library mixes, history, pinned playlists and artists": "资料库混合、历史记录、置顶播放列表和艺人",
    "YouTube Feed": "YouTube 内容",
    "Recommendations, mixes, community playlists and new releases": "推荐、混合、社区播放列表和新发行",
    "These effects may increase CPU and GPU usage.": "这些效果可能会增加 CPU 和 GPU 占用。",
    "Sign in and sync a chat or channel": "登录并同步聊天或频道",
    "Connected to YouTube Music": "已连接 YouTube Music",
    "Connecting…": "正在连接…",
    "Using a direct connection.": "正在使用直连。",
    "Proxy connected.": "代理已连接。",
    "Couldn't connect to the proxy.": "无法连接到代理。",
    "Search songs, artists, albums and playlists on YouTube Music.": "在 YouTube Music 中搜索歌曲、艺人、专辑和播放列表。",
    "Search songs, artists, albums and playlists in your library.": "在你的资料库中搜索歌曲、艺人、专辑和播放列表。",
    "Tap + to add a YouTube or Spotify playlist.": "点按 + 添加 YouTube 或 Spotify 播放列表。",
    "Couldn't load YouTube Music. Tap to try again.": "无法加载 YouTube Music，点按重试。",
    "Playing next": "下一首播放",
}

# File-specific one-word/short replacements that are known to be display text.
file_maps = {
    "navigation/ClassicDock.kt": {
        "Home": "主页", "Discover": "发现", "Search": "搜索", "Library": "资料库",
        "Pause": "暂停", "Play": "播放", "Next": "下一首",
    },
    "library/HomeScreen.kt": {
        "Home": "主页", "Settings": "设置", "Liked": "喜欢", "Downloaded": "已下载",
        "Shuffle": "随机播放", "Recently Played": "最近播放", "Made for You": "为你推荐",
        "Daily Mix": "每日混合", "Rediscover": "重新发现", "Recently Added": "最近添加",
        "Top Artists": "热门艺人", "New releases": "新发行", "See All": "查看全部",
    },
    "library/LibraryHomeScreen.kt": {
        "Library": "资料库", "Settings": "设置", "Playlists": "播放列表", "Artists": "艺人",
        "Albums": "专辑", "Songs": "歌曲", "Downloads": "下载", "Local music": "本地音乐",
        "Pinned": "已置顶", "Recently added": "最近添加", "YouTube Playlists": "YouTube 播放列表",
        "See all": "查看全部", "Create playlist": "新建播放列表",
    },
    "search/SearchScreen.kt": {
        "Discover": "发现", "Your Imported Playlists": "你导入的播放列表",
        "Import playlist": "导入播放列表", "Browse Categories": "浏览分类", "Playing next": "下一首播放",
    },
    "settings/SettingsScreen.kt": {
        "Settings": "设置", "Accounts": "账号", "Connected": "已连接", "Sign In": "登录",
        "Home Feeds": "主页内容", "Appearance": "外观", "Now Playing": "正在播放", "Library": "资料库",
        "App Storage": "应用存储", "Cancel": "取消", "Change Account": "切换账号", "Sign Out": "退出登录",
    },
}

changed = 0
for path in ui_root.rglob("*.kt"):
    rel = path.relative_to(ui_root).as_posix()
    text = path.read_text(encoding="utf-8")
    original = text
    mapping = dict(common)
    mapping.update(phrases)
    mapping.update(file_maps.get(rel, {}))
    # Exact Kotlin string-literal replacements only.
    for old, new in sorted(mapping.items(), key=lambda kv: len(kv[0]), reverse=True):
        text = text.replace('"' + old.replace('"', '\\"') + '"', '"' + new.replace('"', '\\"') + '"')
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed += 1

# Android widget strings are centralized in XML.
strings = root / "app/src/main/res/values/strings.xml"
xml = strings.read_text(encoding="utf-8")
xml_map = {
    "TeleMusic Small": "TeleMusic 小组件（小）",
    "TeleMusic Medium": "TeleMusic 小组件（中）",
    "TeleMusic Large": "TeleMusic 小组件（大）",
    "Cover and play button": "封面和播放按钮",
    "Now playing with controls": "正在播放与控制按钮",
    "Controls, Like and up next": "控制、喜欢和接下来播放",
}
for old, new in xml_map.items():
    xml = xml.replace(">" + old + "<", ">" + new + "<")
strings.write_text(xml, encoding="utf-8")

print(f"Localized {changed} Kotlin UI files + strings.xml")

# Audit likely display strings left in UI. This is informational and does not fail the build.
string_re = re.compile(r'"((?:\\.|[^"\\])*)"')
skip_parts = ("http://", "https://", "content://", "android.", "com.", "application/", "image/", "audio/", "video/", "yyyy", "HH:", "UTF-", "Bearer ")
seen = set()
for path in ui_root.rglob("*.kt"):
    rel = path.relative_to(ui_root).as_posix()
    text = path.read_text(encoding="utf-8")
    for m in string_re.finditer(text):
        s = m.group(1)
        if not re.search(r"[A-Za-z]", s):
            continue
        if any(p in s for p in skip_parts):
            continue
        if s.startswith(("route_", "item_", "section_")):
            continue
        # Likely human-facing if it contains whitespace/punctuation or starts uppercase.
        if not (" " in s or (s and s[0].isupper())):
            continue
        key = (rel, s)
        if key in seen:
            continue
        seen.add(key)
        if len(seen) <= 700:
            print(f"UNTRANSLATED? {rel}: {s}")
