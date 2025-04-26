    // Project Modal Script
    function openModal(name, description, link, feedback) {
      console.log("Hellou");
        document.getElementById('projectModalLabel').innerText = name;
        document.getElementById('modalDescription').innerText = description;
        document.getElementById('modalLink').href = link;
        document.getElementById('modalFeedback').innerText = feedback;
        new bootstrap.Modal(document.getElementById('projectModal')).show();
      }

      function submitForm(event) {
        event.preventDefault();
    
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();
        const alertBox = document.getElementById('alert');
    
        if (name && email && message) {
          fetch('/messages', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, message })
          })
          .then(response => {
            return response.json().then(data => {
              if (response.ok) {
                alertBox.style.display = 'block';
                alertBox.className = 'alert alert-success';
                alertBox.innerText = 'Xabaringiz muvaffaqiyatli yuborildi!';
                document.getElementById('contact-form').reset();
                console.log('✅ Server javobi:', data);
              } else {
                throw new Error(data.message || 'Xatolik yuz berdi');
              }
            });
          })
          .catch(error => {
            console.log(error);
            
            alertBox.style.display = 'block';
            alertBox.className = 'alert alert-danger';
            alertBox.innerText = 'Xatolik yuz berdi. Qayta urinib ko‘ring.';
            console.error('❌ Xatolik:', error);
          });
        } else {
          alertBox.style.display = 'block';
          alertBox.className = 'alert alert-danger';
          alertBox.innerText = 'Iltimos, barcha maydonlarni to\'ldiring.';
        }
      }
      
      const filterButtons = document.querySelectorAll('.filter-btn');
      filterButtons.forEach(button => {
        button.addEventListener('click', function() {
          const category = this.getAttribute('data-category');
          const projects = document.querySelectorAll('.project-card');
          
          projects.forEach(project => {
            if (category === 'all' || project.getAttribute('data-category') === category) {
              project.style.display = 'block';
            } else {
              project.style.display = 'none';
            }
          });
        });
      });

      window.addEventListener('DOMContentLoaded', function () {
        const audio = document.getElementById('bg-music');
        audio.volume = 0.3;
        audio.play().catch(function (e) {
          console.log("Autoplay bloklandi, foydalanuvchi interaction kerak:", e);
        });
      });

      var typed = new Typed(".pro-text", {
        strings: [
            "Ethical Hacker",
            "Penetration Tester",
            "Linux Administrator",
            "Competitive Programmer",
            "Typer",
            "DevOps",
            "Python Developer"
        ],
        typeSpeed: 50,
        backSpeed: 20,
        backDelay: 1000,
        loop: true
    });