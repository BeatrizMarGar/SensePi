import { useState, useEffect } from 'react'

function SensorPanel(){

	const [data, setData] = useState(null)
	const [loading, setLoading] = useState(true)
	const [error, setError] = useState(null)


	useEffect(() => {
	
		const fetchSensor = async () => {
			try {
				const res = await fetch('http://10.1.1.162:3001/sensor')
				if (!res.ok) throw new Error ('Error del servidor')
				const json = await res.json()
				setData(json)
				setError(null)
			} catch (err) {
				setError(err.message)
			} finally{
				setLoading(false)
			}
		}
	
	fetchSensor()

	const intervalo = setInterval(fetchSensor, 2000)
	return () => clearInterval(intervalo)
	}, [])

	if (loading) return <p>Cargando información del sensor...</p>
	if (error) return <p>Error: {error}</p>

	return (
		<div>
			<h2>Sensor DHT11</h2>
			<p>Temperatura: {data.temperatura} ºC</p>
			<p>Humedad: {data.humedad} %</p>
			<p>Estado: {data.estado}</p>
		</div>

	)}	

export default SensorPanel
