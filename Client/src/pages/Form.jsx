import React, { useState } from 'react';

function Form({ onSubmitForm }) {
  const [formData, setFormData] = useState({
    criminalName: '',
    dateOfArrest: '',
    crimeCommitted: '',
    officerInCharge: '',
    officerId: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    alert('Submitted');

    // Send form data to the Flask API using fetch
    fetch('http://127.0.0.1:5000/api/crimes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Crime data submitted:', data);

      onSubmitForm(data);
      
      // Optionally, you can reset the form after successful submission
      setFormData({
        criminalName: '',
        dateOfArrest: '',
        crimeCommitted: '',
        officerInCharge: '',
        officerId: ''
      });
    })
    .catch(error => console.error('Error submitting crime data:', error));
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  return (
    <div className='form-container'>
      <div className='form'>
        <form onSubmit={handleSubmit}>
          <div>
            <label>
              Criminal Name:
              <input
                type="text"
                name="criminalName"
                value={formData.criminalName}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Date Of Arrest:
              <input
                type="text"
                name="dateOfArrest"
                value={formData.dateOfArrest}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Crime Committed:
              <input
                type="text"
                name="crimeCommitted"
                value={formData.crimeCommitted}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Officer in Charge:
              <input
                type="text"
                name="officerInCharge"
                value={formData.officerInCharge}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Officer id:
              <input
                type="text"
                name="officerId"
                value={formData.officerId}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default Form;
