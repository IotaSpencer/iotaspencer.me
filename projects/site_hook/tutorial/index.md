---
layout: page
title: site_hook - Tutorial
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

#### Notes on Usage
* You must at least have a 'Gemfile' as the jekyll command used requires it
* Clone your site to where you want it built from
* **IMPORTANT**: Run `bundle install --path vendor/bundle`{:.highlight}
    otherwise you may get dependency errors

#### Generating a Project Block
To generate a project block, (using the latest version of site_hook).
* `site_hook config gen-project`{:.highlight}

This command will ask you questions and spit out an indent block to put into your `~/.jph/config`{:.highlight} file.

This command also gives you a hook password/token/secret.
* If you don't like the string that was generated, then you can change it once you've copied the rest to your config.

### Start

  If a configuration file has been created and/or generated(then edited correctly)... using 'server listen'
  should initiate the webhook and have it start
#### Multiplexer Usage
**NOTE**: I would suggest running the 'listen' command in a `screen`{:.highlight} or `tmux`{:.highlight} session.
  This is due to the output of logs and due to the fact that the gem is not a daemon.
* `tmux new -s site_hook`{:.highlight}
* `screen -mS site_hook`{:.highlight}

#### Starting Syntax

* `site_hook server listen`{:.highlight}
  <hr class="d-flex justify-content-center hr-text" data-content="or">

* `bundle exec site_hook server listen`{:.highlight}

Depending on how you installed site_hook.
</div>