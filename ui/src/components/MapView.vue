<template>
  <div id="map"></div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import maplibregl from 'maplibre-gl';

let map: maplibregl.Map;

const formData = ref({
  nom: '',
  preu: '',
  url: '',
});

const popupContent = `
    <div style="display: flex; flex-direction: column; width: 200px;">
      <label>Nom:</label>
      <input id="nomInput" type="text" placeholder="Introdueix el nom" />
      <label>Preu:</label>
      <input id="preuInput" type="number" placeholder="Introdueix el preu" />
      <label>URL:</label>
      <input id="urlInput" type="text" placeholder="Enter URL" />
      <button id="submitButton">Submit</button>
    </div>
  `;

// const houseIcon = `
//   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="32" height="32">
//   <path d="M12 3l9 9-1.5 1.5L18 11.5V20h-5v-5H11v5H6v-8.5L4.5 13.5 3 12l9-9z"/>
//   </svg>
// `;
const onSubmit = () => {
  console.log('Form submitted');
  console.log('Form Data:', formData.value);
  // You can store this data or perform any other action with it
};

const showPopup = (coords: [number, number]) => {
  const popup = new maplibregl.Popup()
    .setLngLat(coords)
    .setHTML(popupContent)
    .addTo(map);
  
  document.getElementById('submitButton')?.addEventListener('click', () => {
    const nomInput = (document.getElementById('nomInput') as HTMLInputElement).value;
    const preuInput = (document.getElementById('preuInput') as HTMLInputElement).value;
    const urlInput = (document.getElementById('urlInput') as HTMLInputElement).value;

    formData.value = { nom: nomInput, preu: preuInput, url: urlInput };

    onSubmit();
    popup.remove();
  });
  
  // The below listeners do not seem to be triggered.
  popup.on('open', () => {
    console.log("Popup opened");
  });
  popup.on('close', () => {
    console.log('popup was closed');
  });
};

const onClick = (e: maplibregl.MapMouseEvent) => {
  const coords = [e.lngLat.lng, e.lngLat.lat] as [number, number];
  showPopup(coords);
  // console.log('Coordinates: ', coords);
  // clickedCoordinates.value.push(coords);

  // const el = document.createElement('div');
  // el.innerHTML = houseIcon;
  // el.style.width = '32px';
  // el.style.height = '32px';
  // el.style.backgroundColor = 'transparent';
  // const marker = new maplibregl.Marker({ element: el }).setLngLat(coords).addTo(map);
  // console.log('Marker added: ', marker);
};

onMounted(() => {
  const bounds = [
        [2.0, 41.3],
        [2.3, 41.5],
      ];
    map = new maplibregl.Map({
      container: 'map',
      style: 'https://api.maptiler.com/maps/topo-v2/style.json?key=it8NWjb5IFkKJfa2gPI8',
      center: [2.1734, 41.3851],
      zoom: 6,
      bounds: bounds,
    });

    map.on('load', () => {
      map.on('click', onClick);
    });
});

</script>

<style>
#map {
  width: 100%;
  height: 100vh;
}
</style>