import { useState, ChangeEvent } from 'react';
import { setTargetMoisture } from '../services/api';

const MoistureConfiguration = () => {
  const [level, setLevel] = useState<number>(50);
  const [message, setMessage] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const handleSetLevel = async () => {
    setLoading(true);
    setMessage(''); // Clear previous message
    try {
      const response = await setTargetMoisture(level);
      setMessage(response.message);
    } catch (error) {
      setMessage('Failed to set moisture level.');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setLevel(parseInt(e.target.value, 10));
  };

  return (
    <div className="moisture-config-section">
      <h2>Configure Target Moisture</h2>
      <div className="config-container moisture-config-controls">
        <input
          type="range"
          min="0"
          max="100"
          value={level}
          onChange={handleChange}
          disabled={loading}
        />
        <span>{level}%</span>
      </div>
      <button onClick={handleSetLevel} disabled={loading}>
        {loading ? 'Setting...' : 'Set Level'}
      </button>
      
    </div>
  );
};

export default MoistureConfiguration;