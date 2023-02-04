import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [result, setResult] = useState('');

  const handleFileChange = e => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    axios
      .post("http://localhost:5000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
      .then(res => setResult(res.data.result))
      .catch(err => console.log(err));
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <p>{result}</p>
    </div>
  );
}

export default
