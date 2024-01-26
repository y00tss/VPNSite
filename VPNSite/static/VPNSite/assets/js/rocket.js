function openIframeInNewTab() {
            var newTab = window.open('https://rezka.ag/page/9/', '_blank');
            if (newTab) {
                newTab.focus();
            } else {
                alert('Ваш браузер заблокировал открытие новой вкладки. Разрешите это в настройках.');
            }
        }

