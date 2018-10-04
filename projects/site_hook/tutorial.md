---
layout: page
title: site_hook
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

## Installation

* `gem install site_hook`{:.highlight}

  <hr class="hr-text d-flex justify-content-center" data-content="or">

1. `git clone https://github.com/IotaSpencer/site_hook`{:.highlight}

1. `cd site_hook`{:.highlight}

1. Install
    1. Bundler
      * `bundle install --system`{:.highlight}
    1. Gem
    * First `gem build site_hook.gemspec`{:.highlight}
      * then `gem install site_hook-x.x.x.gem`{:.highlight} to install to system (as root)
      * `sudo gem install site_hook-x.x.x.gem`{:.highlight} to install to system when a sudoer
      * `gem install site_hook-x.x.x.gem --user-install`{:.highlight} to install as current user (to user GEM_HOME)

## Setup

### Create Needed Files & Directories
* Backup any previous site_hook configs
* `site_hook config gen`{:.highlight}
  * This will create the following files and directories.
    * `~/.jph/`{:.highlight}

## Usage

#### Notes on Usage
* You must at least have a 'Gemfile' as the jekyll command used requires it
* Clone your site to where you want it built from
* **IMPORTANT**: Run `bundle install --path vendor/bundle`{:.highlight}
    otherwise you may get dependency errors

### Start

  If a configuration file has been created and/or generated(then edited correctly)... using 'server listen' should initiate the webhook and have it start

* `site_hook server listen`{:.highlight}
  <hr class="d-flex justify-content-center hr-text" data-content="or">

* `bundle exec site_hook server listen`{:.highlight}

Depending on how you installed site_hook.
</div>