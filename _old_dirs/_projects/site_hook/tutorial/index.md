---
layout: page
title: Tutorial
permalink: projects/site_hook/tutorial/index.html
breadcrumb: Tutorial
excerpt: SiteHook is a RubyGem that is used to pull jekyll blogs and build them as a intermediary between a git service webhook and a production server.
tags:
- jekyll
- site_hook
- ruby
- gem
- rubygems
page_links:
  'site_hook on RubyGems.org': https://rubygems.org/gems/site_hook
  GitHub: https://github.com/IotaSpencer/site_hook
---
<div class="float-right card bg-dark ml-4 mr-2" style="order: 2;" markdown="1">

# Contents
{:.no_toc .mx-auto}

* TOC
{:toc class="well bg-dark d-inline-block pr-3 py-3"}
</div>

<div markdown="1">
# {{ page.title }}

**Note**: This tutorial is for < 0.9.2, see [/projects/site_hook/guide/](/projects/site_hook/guide/) for > 0.9.2
{:.alert .alert-danger .d-inline-block}

## Installation

* `gem install site_hook`{:.highlight}

Support is only given when using the latest version unless you are explicitly trying to help develop site_hook,
for helping develop site_hook, please go [>here<](/projects/site_hook/developing/)

## Setup

### Create Needed Files & Directories
* Backup any previous site_hook configs
* Run `site_hook config gen`{:.highlight}
  * This will create the following files and directories.
    * `~/.jph/`{:.highlight}
    * `~/.jph/config`{:.highlight}
    * `~/.jph/logs`{:.highlight}

## Usage
  <a href="{% link projects/site_hook/tutorial/usage/index.md %}">Please go here for usage and Starting.</a>
</div>