'use client'

import Map from 'react-map-gl/mapbox'
import 'mapbox-gl/dist/mapbox-gl.css'

export default function MapView() {
  return (
    <Map
      mapboxAccessToken={process.env.NEXT_PUBLIC_MAPBOX_TOKEN}
      initialViewState={{
        longitude: -122.3321,
        latitude: 47.6062,
        zoom: 11,
      }}
      style={{ width: '100%', height: '100%' }}
      mapStyle="mapbox://styles/mapbox/light-v11"
    />
  )
}
