import React from 'react'
import Form from '../pages/Form'; // Import your Form component
import Tables from '../pages/Tables'; // Import your CrimeTable component


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
      <Tables crimes={crimes} />
    </div>
  )
}

export default ParentComponent;
