# 🎮 Juego de Naves en Pygame

Este es mi primer acercamiento al desarrollo de videos juegos, con un clásico juego arcade tipo *"Shooter"*, desarrollado en **Python** con la librería **Pygame**. Se controla una nave que dispara láseres para destruir meteoritos que van cayendo. El objetivo es no perder todas las vidas, evitando los choques y sumar la mayor cantidad de puntos posibles

---

## 📸 Captura de pantalla

<img width="778" height="623" alt="image" src="https://github.com/user-attachments/assets/d83c9712-f6b6-406a-a393-04afeeeb7aa8" />


---

## 🚀 Características

- Movimiento lateral del jugador.
- Disparo de proyectiles con sonido.
- Meteoritos con apariciones aleatorias y distintas velocidades.
- Sistema de vidas/escudo visual con barra.
- Explosiones animadas al destruir meteoritos.
- Música de fondo y efectos de sonido.
- Pantalla de inicio con instrucciones.
- Sistema de puntaje.
- Detección de colisiones (jugador/meteoro y bala/meteoro).

---

## 🎮 Controles

- ⬅️ / ➡️ — Mover la nave izquierda/derecha  
- Barra espaciadora — Disparar  
- Enter — Comenzar el juego desde la pantalla inicial  

---

## 🧱 Estructura del código

- `Player`: controla el movimiento y disparo del jugador.
- `Meteor`: genera meteoritos de distintos tamaños, que caen con distinta velocidad y dirección.
- `Bullet`: lasers que destruyen a los meteoritos.
- `Explosion`: animación cuando un meteorito es destruido.
- `draw_text` / `draw_shield_bar`: utilidades para mostrar texto y la barra de escudo.
- `show_go_screen`: pantalla de bienvenida/intermedio.

---

### Instalación de dependencias:
```bash
pip install pygame

