import { useState } from 'react'

function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex)
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : { r: 0, g: 0, b: 0 }
}

function LedControl() {
  const [color, setColor] = useState('#ff0000')
  const [encendido, setEncendido] = useState(false)
  const [cargando, setCargando] = useState(false)

  const enviarComando = async (nuevoEstado) => {
    setCargando(true)
    const rgb = hexToRgb(color)
    try {
      await fetch('http://10.1.1.162:3001/led', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          r: rgb.r,
          g: rgb.g,
          b: rgb.b,
          encendido: nuevoEstado
        })
      })
      setEncendido(nuevoEstado)
    } catch (err) {
      console.error('Error al controlar el LED:', err)
    } finally {
      setCargando(false)
    }
  }

  return (
    <div>
      <h2>Control LED</h2>
      <input
        type="color"
        value={color}
        onChange={(e) => setColor(e.target.value)}
      />
      <button
        onClick={() => enviarComando(!encendido)}
        disabled={cargando}
      >
        {cargando ? 'Enviando...' : encendido ? 'Apagar' : 'Encender'}
      </button>
      <div style={{
        width: '100px',
        height: '100px',
        backgroundColor: encendido ? color : '#000000',
        border: '1px solid #ccc',
        marginTop: '10px'
      }} />
      <p>{encendido ? `Encendido: ${color}` : 'Apagado'}</p>
    </div>
  )
}

export default LedControl
