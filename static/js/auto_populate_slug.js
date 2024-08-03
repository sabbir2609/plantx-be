document.addEventListener('DOMContentLoaded', function() {
    var userSelect = document.getElementById('id_user');
    var slugField = document.getElementById('id_slug');

    if (userSelect) {
        userSelect.addEventListener('change', function() {
            var userId = userSelect.value;

            // Make an AJAX call to fetch the full name of the selected user
            if (userId) {
                fetch(`/admin/get_user_full_name/${userId}/`)
                    .then(response => response.json())
                    .then(data => {
                        var fullName = data.full_name;
                        var slug = slugify(fullName);
                        slugField.value = slug;
                    });
            }
        });
    }

    function slugify(text) {
        return text.toString().toLowerCase()
            .replace(/\s+/g, '-')           // Replace spaces with -
            .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
            .replace(/\-\-+/g, '-')         // Replace multiple - with single -
            .replace(/^-+/, '')             // Trim - from start of text
            .replace(/-+$/, '');            // Trim - from end of text
    }
});
