---
layout: page
title: site_hook
permalink: projects/site_hook/developing/index.html
breadcrumb: site_hook
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
