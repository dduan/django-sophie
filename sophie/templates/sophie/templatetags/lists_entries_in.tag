{% for entry in entries %}
    <h2><a href="{{ entry.get_absolute_url }}">{{ entry.title }}</a></h2>
    <div class="entry-meta-info">
        Published @
        <span class="entry-pub-time">
            {{ entry.pub_date|date:"DATETIME_FORMAT" }}
        </span>
        by
        <span class="entry-author">{{ entry.author.get_full_name}}</span>
    </div>
    <div class="entry-body">
    {% if blog.full_entry_in_page %}
        {{ entry.body_html|safe }}
    {% else %}
        {{ entry.teaser_html|safe }}
    {% endif %}
    </div>
{% empty %}
<div id="emptypage-description">
    {{ empty_msg }}
</div>
{% endfor %}
