---
layout: page
title: site_hook
permalink: projects/site_hook/index.html
breadcrumb: site_hook
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
{:toc class="well bg-dark d-inline-block pr-3 py-2"}
</div>

<div markdown="1">
# {{ page.title }}

## Installation

  <div class="list-group bg-dark-gray d-flex">

  <div markdown="1" class="list-group-item bg-dark-gray d-flex">

  `gem install site_hook`{:.highlight}

  </div>

  <div class="list-group-item bg-dark-gray d-flex mx-auto">or</div>

  <div markdown="1" class="list-group-item bg-dark-gray d-flex">

  1. `git clone https://github.com/IotaSpencer/site_hook`{:.highlight}

  1. `cd site_hook`{:.highlight}

  1. Install
     * `bundle install --system`{:.highlight}
     * `gem build site_hook.gemspec`{:.highlight}
     then
     * `gem install site_hook-x.x.x.gem`{:.highlight} to install to system (as root)
     or
     * `sudo gem install site_hook-x.x.x.gem`{:.highlight} to install to system when a sudoer
     or
     * `gem install site_hook-x.x.x.gem --user-install`{:.highlight} to install as current user (to user GEM_HOME)
  </div>

  </div>

## Setup

### Create Needed Files & Directories
* Create a file named `.jph-rc`{:.highlight} in the home
    directory of the user that's going to be running the site_hook
    You can either do this using
  <div class="list-group bg-dark-gray d-flex">

  <div markdown="1" class="list-group-item bg-dark-gray d-flex">

  `site_hook config gen > ~/.jph-rc`{:.highlight}

  To redirect the output to a file.
  </div>

  <div class="mx-auto d-flex">or</div>

  <div markdown="1" class="list-group-item bg-dark-gray d-flex">

  `site_hook config gen -f`{:.highlight}

  To force a file to be created by the script.
  </div>

  </div>

* Create a directory named `.jph`{:.highlight} in the same home directory.

## Usage

### Start

  If a configuration file has been created or generated(then edited correctly)... using 'start' should initiate the webhook and have it start

  <div class="list-group bg-dark-gray d-block">

  <div markdown="1" class="list-group-item bg-dark-gray d-flex">

  `site_hook config gen > ~/.jph-rc`{:.highlight}

  To redirect the output to a file.
  </div>

  <div class="mx-auto d-flex">or</div>

  <div markdown="1" class="list-group-item bg-dark-gray d-flex">

  `site_hook config gen -f`{:.highlight}

  To force a file to be created by the script.
  </div>

  </div>
</div>