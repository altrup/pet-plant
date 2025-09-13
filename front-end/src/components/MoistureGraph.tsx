import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { getMoistureLevels } from '../services/api';

interface MoistureData {
  name: string;
  level: number;
}

const MoistureGraph = () => {
  const [data, setData] = useState<MoistureData[]>([]);

  useEffect(() => {
    getMoistureLevels().then(setData);
  }, []);

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart
        data={data}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" stroke="var(--color-grid)" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip
          wrapperStyle={{ 
            backgroundColor: 'var(--color-card-background)',
            border: '1px solid var(--color-primary)'
          }}
          contentStyle={{ color: 'var(--color-text)' }}
          labelStyle={{ color: 'var(--color-text)' }}
        />
        <Legend />
        <Line type="monotone" dataKey="level" stroke="var(--color-primary)" activeDot={{ r: 8 }} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default MoistureGraph;
