import React, { useState, useEffect } from 'react';



function CrimeTable({  }) {
  const [crimes, setCrimes] = useState([]);

  useEffect(() => {
    // Fetch data from the Flask server when the component mounts
    fetch('http://127.0.0.1:5000/crimes')
      .then(response => response.json())
      .then(data => setCrimes(data))
      .catch(error => console.error('Error fetching crime data:', error));
  }, []); // Empty dependency array ensures the effect runs once after the initial render

  return (
    <div className='table-container'> {/* Apply the table-container class */}
      <h2 className='table-header'>Crime Data Table</h2> {/* Apply the table-header class */}
      <table>
        <thead>
          <tr>
            <th className='table-header'>ID</th> {/* Apply the table-header class */}
            <th className='table-header'>Name</th> {/* Apply the table-header class */}
            <th className='table-header'>Description</th> {/* Apply the table-header class */}
            <th className='table-header'>Victims</th> {/* Apply the table-header class */}
            <th className='table-header'>Criminals</th> {/* Apply the table-header class */}
          </tr>
        </thead>
        <tbody>
          {crimes.map(crime => (
            <tr key={crime.id}>
              <td className='table-data'>{crime.id}</td> {/* Apply the table-data class */}
              <td className='table-data'>{crime.name}</td> {/* Apply the table-data class */}
              <td className='table-data'>{crime.description}</td> {/* Apply the table-data class */}
              <td className='table-data'>{crime.victims.map(victim => victim.name).join(', ')}</td> {/* Apply the table-data class */}
              <td className='table-data'>{crime.criminals.map(criminal => criminal.name).join(', ')}</td> {/* Apply the table-data class */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CrimeTable;
