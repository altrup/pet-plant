const API_BASE_URL: string = import.meta.env.VITE_API_BASE_URL;

// Mock data for the moisture level graph
interface MoistureData {
  name: string;
  level: number;
}

const mockMoistureData: MoistureData[] = [
  { name: '6 hours ago', level: 45 },
  { name: '5 hours ago', level: 50 },
  { name: '4 hours ago', level: 55 },
  { name: '3 hours ago', level: 60 },
  { name: '2 hours ago', level: 58 },
  { name: '1 hour ago', level: 55 },
  { name: 'Now', level: 52 },
];

export const getMoistureLevels = async (): Promise<MoistureData[]> => {
  // In the future, this will make a request to the backend
  // const response = await fetch(`${API_BASE_URL}/moisture`);
  // const data = await response.json();
  // return data;

  // For now, return mock data
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(mockMoistureData);
    }, 500);
  });
};

interface SetTargetMoistureResponse {
  success: boolean;
  message: string;
}

export const setTargetMoisture = async (level: number): Promise<SetTargetMoistureResponse> => {
  // In the future, this will make a request to the backend
  /*
  const response = await fetch(`${API_BASE_URL}/config`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ targetMoisture: level }),
  });
  const data = await response.json();
  return data;
  */

  // For now, just log the level and return a success message
  console.log(`Setting target moisture to ${level}`);
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({ success: true, message: `Target moisture set to ${level}` });
    }, 500);
  });
};