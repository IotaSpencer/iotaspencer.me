### Social Media
{% for service in site.data.contact.sites %}
{{service}}
<div class="container">
    <a href="{{ service.url }}">
        <i class="{{service.class }}"></i>
        {{ service.extra }}
    </a>
</div>
{% endfor %}

## Other Stuff

<div class="container"> Don't do IRC anymore
<a href="[REDACTED]">
<i class="fas fa-hashtag fa-2x"></i>
IRC
</a>
</div>
<div class="container">
<i class="fas fa-key fa-2x"></i>
<a href="/gnupg">
GNUPG Key
</a>
</div>