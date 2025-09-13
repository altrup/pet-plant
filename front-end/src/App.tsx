import { useState, useEffect } from 'react';
import './App.css';
import MoistureConfiguration from './components/MoistureConfiguration';
import MoistureGraph from './components/MoistureGraph';
import ThemeSwitch from './components/ThemeSwitch';

function App() {
  const [theme, setTheme] = useState(() => {
    const savedTheme = localStorage.getItem('theme');
    return savedTheme || 'dark';
  });

  useEffect(() => {
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(theme === 'dark' ? 'light' : 'dark');
  };

  return (
    <div className={`App ${theme}-theme`}>
      <header className="App-header">
        <h1>Pet Plant</h1>
        <ThemeSwitch theme={theme} toggleTheme={toggleTheme} />
      </header>
      <main>
        <div className="card">
          <h2>Moisture Level Over Time</h2>
          <MoistureGraph />
        </div>
        <div className="card">
          <MoistureConfiguration />
        </div>
      </main>
    </div>
  );
}

export default App;