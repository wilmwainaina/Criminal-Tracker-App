import React from 'react'
import Form from './Form'; // Import your Form component
import CrimeTable from './CrimeTable'; // Import your CrimeTable component


function ParentComponent() {
    const [crimes, setCrimes] = useState([]);

    const handleFormSubmit = (submittedData) => {
        // Update the crimes state with the submitted data
        setCrimes([...crimes, submittedData]);
    };
  return (
    <div>
       {/* Render the Form component and pass the handleFormSubmit function as a prop */}
       <Form onSubmitForm={handleFormSubmit} />
      {/* Render the CrimeTable component and pass the crimes data as a prop */}
      <CrimeTable crimes={crimes} />
    </div>
  )
}

export default ParentComponent;
