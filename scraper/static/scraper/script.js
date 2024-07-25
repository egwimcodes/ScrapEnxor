document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('scrapeForm');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const companyName = document.getElementById('companyName');
    const logo = document.getElementById('logo');
    const logoUrl = document.getElementById('logoUrl');
    const contactInfo = document.getElementById('contactInfo');
    const aboutCompany = document.getElementById('aboutCompany');
    const location = document.getElementById('location');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        loading.style.display = 'block';
        result.style.display = 'none';

        const formData = new FormData(form);
        const url = formData.get('url');

        const csrftoken = getCookie('csrftoken');

        fetch('/scrape/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                loading.style.display = 'none';
                result.style.display = 'block';

                if (data.error) {
                    console.error('Error:', data.error);
                }

                const getDomainName = (url) => {
                    const anchor = document.createElement('a');
                    anchor.href = url;
                    return anchor.origin;
                };

                const domainName = getDomainName(url);

                companyName.textContent = data.company_name || 'N/A';

                let logoSource = data.logo_url || 'N/A';
                if (logoSource !== 'N/A' && !logoSource.startsWith('http://') && !logoSource.startsWith('https://')) {
                    logoSource = domainName + logoSource;
                }
                logo.src = logoSource;
                logoUrl.textContent = logoSource;

                aboutCompany.textContent = data.about_company || 'N/A';
                location.textContent = data.location || 'N/A';

                contactInfo.innerHTML = '';
                if (data.contact_info.phone_numbers.length > 0) {
                    contactInfo.innerHTML += `<li>Phone Numbers: ${data.contact_info.phone_numbers.join(', ')}</li>`;
                }
                if (data.contact_info.emails.length > 0) {
                    contactInfo.innerHTML += `<li>Emails: ${data.contact_info.emails.join(', ')}</li>`;
                }
                if (data.contact_info.phone_numbers.length === 0 && data.contact_info.emails.length === 0) {
                    contactInfo.innerHTML = 'N/A';
                }
            })
            .catch(error => {
                loading.style.display = 'none';
                console.error('Error:', error);
            });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
