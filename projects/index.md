---
layout: page
title: Projects
projects:
  - name: Jekyllposter
    link: /projects/jekyllposter
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

## {{project.name}}

A Ruby package (usually known as a gem) for generating jekyll posts and pages, as well as drafts.

> [Link]({{project.link}})

{% endfor %}