const img = document.getElementById('movie_image');

movie_image.addEventListener('error', function handleError() {
  const defaultImage =
    'https://image.tmdb.org/t/p/w500//tLFIMuPWJHlTJ6TN8HCOiSD6SdA.jpg';

  movie_image.src = defaultImage;
  movie_image.alt = 'default';
});