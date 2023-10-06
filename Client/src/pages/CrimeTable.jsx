import React from 'react';

function CrimeTable({ crimes }) {
  return (
    <div className='table-container'>
      <h2 className='table-header'>Crime Data Table</h2>
      <table>
        <thead>
          <tr>
            <th className='table-header'>ID</th>
            <th className='table-header'>Name</th>
            <th className='table-header'>Description</th>
            <th className='table-header'>Victims</th>
            <th className='table-header'>Criminals</th>
          </tr>
        </thead>
        <tbody>
          {crimes.map(crime => (
            <tr key={crime.id}>
              <td className='table-data'>{crime.id}</td>
              <td className='table-data'>{crime.name}</td>
              <td className='table-data'>{crime.description}</td>
              <td className='table-data'>{crime.victims.map(victim => victim.name).join(', ')}</td>
              <td className='table-data'>{crime.criminals.map(criminal => criminal.name).join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CrimeTable;

