{% if page.has_other_pages %}
<span id="which-page">
 This is {{ page }}
</span>
{% if page.has_next %}
<span id="next-page-link">
    <a href="{{ next_link }}">[Older Posts]</a>
</span>
{% endif %}
{% endif %}
{% if page.has_previous %}
<span id="previous-page-link">
    <a href="{{ previous_link }}">[Newer Posts]</a>
</span>
{% endif %}
