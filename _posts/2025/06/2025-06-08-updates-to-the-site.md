---
layout: post
title: Updates To The Site!
excerpt: |-
  There have been a large amount of changes to the site, this posts goes through almost all of them.
tags:
- updates
- posts
categories:
- Updates
summary: |-
  There have been a large amount of changes to the site,
  this posts goes through almost all of them.
description: |-
  There have been a large amount of changes to the site,
  this posts goes through almost all of them.
date: '2025-06-08 04:33:05 -0300'
meta_links: 
  - rel: canonical
    href: https://www.example.com/updates-to-the-site/
  - rel: alternate
    type: application/rss+xml
    href: https://www.example.com/updates-to-the-site/feed.xml

modified: false
  
series: updates_series
---

## Updates To The Site!

There have been a large amount of changes to the site, this posts goes through almost all of them.

### New Theme

The site now has a new theme, which is more modern and responsive. It should look better on mobile devices and tablets.

The theme is based on the bulma theme and CSS framework, which allows for a more flexible and customizable design.
I've also brought in bootstrap for some components, like the navbar, and some cards/card-decks.

### New/Updated Pages

- Projects page has been updated with new projects and a new layout.
- Portfolio page has been updated with new projects and a new layout.
- Activity (Wakatime) page has been updated with a new layout.
- Blog page has been implemented, it now shows the latest posts and has a new layout.

### Easier Deployment

The site is now easier to deploy, with a new deployment script that automates the process.
This should make it easier to update the site and deploy new changes.

### Other Changes
  - mkmatter is shipped with the site, so i can use it to generate pages, posts, and other content.
  - The site now uses a new RSS feed format, which should be more compatible with most RSS readers.

### About Deployment
The script I created is a simple-ish python script, I can serve the local version with `bundle exec jekyll serve` and then run the script to deploy the site.
And then if I like the changes I can run `bin/deploy.py btp` {.highlight} to deploy the site to the production server.

See [the bin directory in the repository](https://github.com/IotaSpencer/iotaspencer.me/tree/master/bin).

