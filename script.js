// Inicialização do Reveal.js
Reveal.initialize({
    hash: true,
    transition: 'slide',
    backgroundTransition: 'fade'
});

// Expansão de imagens e vídeos, vídeos reiniciam automaticamente
document.addEventListener('DOMContentLoaded', function() {
    // Criar overlay para expansão de mídia
    const overlay = document.createElement('div');
    overlay.className = 'image-expand-overlay';
    
    const mediaContainer = document.createElement('div');
    mediaContainer.className = 'image-expand-container';
    
    overlay.appendChild(mediaContainer);
    document.body.appendChild(overlay);
    
    // Adicionar evento de clique para fechar
    overlay.addEventListener('click', function() {
        overlay.style.display = 'none';
        // Pausar vídeo se estiver reproduzindo
        const video = mediaContainer.querySelector('video');
        if (video) {
            video.pause();
        }
        mediaContainer.innerHTML = '';
    });
    
    // Função para adicionar comportamento de reinício automático aos vídeos
    function addVideoAutoRestartBehavior(videoElement) {
        videoElement.addEventListener('ended', function() {
            this.currentTime = 0;
            this.play();
        });
    }
    
    // Adicionar comportamento de reinício automático a todos os vídeos na página
    document.querySelectorAll('video').forEach(video => {
        addVideoAutoRestartBehavior(video);
    });
    
    // Adicionar eventos de clique para todas as imagens e vídeos
    const allMedia = document.querySelectorAll('img, video');
    allMedia.forEach(media => {
        media.addEventListener('click', function(e) {
            e.stopPropagation();
            
            // Limpar container
            mediaContainer.innerHTML = '';
            
            // Clonar elemento para o overlay
            const clonedMedia = this.cloneNode(true);
            
            // Adicionar controles para vídeos
            if (clonedMedia.tagName === 'VIDEO') {
                clonedMedia.setAttribute('controls', true);
                clonedMedia.style.maxWidth = '80%';
                clonedMedia.style.maxHeight = '80%';
                // Adicionar comportamento de reinício automático ao clone
                addVideoAutoRestartBehavior(clonedMedia);
            }
            
            mediaContainer.appendChild(clonedMedia);
            overlay.style.display = 'flex';
            
            // Reproduzir vídeo automaticamente
            if (clonedMedia.tagName === 'VIDEO') {
                clonedMedia.play();
            }
        });
    });
});

// Controles para o tema de inverno
Reveal.addEventListener('ready', function() {
    // Efeito de transição para o slide de inverno
    Reveal.addEventListener('slidechanged', function(event) {
        // Verificar se é o slide do Inverno da IA
        if (event.currentSlide.querySelector('h1') && 
            event.currentSlide.querySelector('h1').textContent === 'Inverno da IA') {
            
            // Aplicar tema de inverno ao corpo
            document.querySelector('.reveal').classList.add('winter-theme');
            
            // Adicionar flocos de neve
            addSnowflakes();
            
        } else {
            // Remover tema de inverno
            document.querySelector('.reveal').classList.remove('winter-theme');
            
            // Remover flocos de neve
            removeSnowflakes();
        }
    });
});

// Função para adicionar flocos de neve
function addSnowflakes() {
    const snowflakes = document.createElement('div');
    snowflakes.className = 'snowflakes';
    
    for (let i = 0; i < 50; i++) {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.innerHTML = '❄';
        snowflake.style.left = Math.random() * 100 + 'vw';
        snowflake.style.animationDuration = (Math.random() * 5 + 5) + 's';
        snowflake.style.fontSize = (Math.random() * 10 + 10) + 'px';
        snowflakes.appendChild(snowflake);
    }
    
    document.querySelector('.reveal').appendChild(snowflakes);
}

// Função para remover flocos de neve
function removeSnowflakes() {
    const snowflakes = document.querySelector('.snowflakes');
    if (snowflakes) {
        snowflakes.remove();
    }
}
