---
layout: page
title: site_hook
permalink: /projects/site_hook
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
{::options parse_block_html="true" /}
<div class="float-right card bg-dark ml-4 mr-2" style="order: 2;">

# Contents
{:.no_toc .mx-auto}

* TOC
{:toc class="well bg-dark d-inline-block pr-3 py-2"}
</div>

<div>

## Setup

1. Create a file named `.jph-rc` in the home
    directory of the user that's going to be running the site_hook

1. Create a directory named `.jph` in the same home directory.

```yaml
log_levels:
  hook: info  # fatal, error, warn, info, debug
  build: info # fatal, error, warn, info, debug
  git: info   # fatal, error, warn, info, debug
  app: info   # fatal, error, warn, info, debug
projects:
  project.name: # as it appears on a github or gitlab or similar service
  # SERVICE.TLD/USER/project.name
    src: /home/user/path/to/jekyll/source
    dst: /path/to/destination
    hookpass: SOMEPASSWORD
```

</div>