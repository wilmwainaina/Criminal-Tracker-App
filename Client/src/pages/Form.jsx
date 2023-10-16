import React, { useState } from 'react';

function Form({ onSubmitForm }) {
  const [formData, setFormData] = useState({
    criminal: '',
    crimes: '',
    victims: '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    alert('Submitted');

    // Send form data to the Flask API using fetch
    fetch('http://127.0.0.1:5000', {
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
        criminal: '',
        crimes: '',
        victims: '',
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
              Criminal:
              <input
                type="text"
                name="criminal"
                value={formData.criminal}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Crimes:
              <input
                type="text"
                name="crimes"
                value={formData.crimes}
                onChange={handleInputChange}
                required
              />
            </label>
          </div>
          <div>
            <label>
              Victims:
              <input
                type="text"
                name="victims"
                value={formData.victims}
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
