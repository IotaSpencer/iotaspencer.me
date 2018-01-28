---
layout: page
title: Projects
breadcrumb: Projects
projects:
  Jekyllposter:
    link: /projects/jekyllposter
    description: "A Ruby package (usually known as a gem) for generating jekyll posts and pages, as well as drafts."

  bot-template:
    link: /projects/bot-template
    description: A template for cinch bots
---
# Projects

## User/Org Links

<a href="https://github.com/IotaSpencer"><span><i class="fab fa-github-square fa-2x"></i> &mdash; GitHub</span>
</a>

<a href="https://gitlab.com/IotaSpencer">
<span color="orange">
<i class="fab fa-gitlab fa-2x"></i>
</span> &mdash; GitLab
</a>

{% for project in page.projects %}

## {{project[0]}}



<dl>
  <dt>Description</dt>
  <dd>{{project[1].description}}</dd>
  <dt>Link</dt>
  <dd><a href="{{project[1].link}}">{{project[1].link}}</a></dd>

</dl>
{% endfor %}