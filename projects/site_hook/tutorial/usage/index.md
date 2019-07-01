---
layout: page
title: Usage
permalink: /projects/site_hook/tutorial/usage/index.html
breadcrumb: Usage
---
## Usage

#### Notes on Usage
* You must at least have a 'Gemfile' as the jekyll command used requires it
* The `Gemfile`{:.highlight} must also include 'jekyll' at the very least, other than the source method

```ruby
source 'https://rubygems.org/'
gem 'jekyll'
```
{:.highlight}

* Clone your site to where you want it built from
* **IMPORTANT**: Run `bundle install --path vendor/bundle`{:.highlight}
    otherwise you may get dependency errors

#### Generating a Project Block
To generate a project block, (using the latest version of site_hook).
* `site_hook config gen-project`{:.highlight}

This command will ask you questions and spit out an indent block to put into your  `~/.jph/config`{:.highlight} file.

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