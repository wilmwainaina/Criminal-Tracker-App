import React from 'react'
import Formasset from '../assets/jailbars-2.jpg';

function Form() {
  return (
    
<div className='form-container'>
    <div className='form'>
    
      <form className=''>
    
    <div className=''>
      <label>
        Criminal Name :   
        <input
          className=''
          type="text"
          placeholder='    Enter criminal name'
        />
      </label>
    </div>

    <div>
      <label className=''>
        Date Of Arrest:
        <input
          type="text"
          className=''
          placeholder='     Enter your Email'
          required
        />
      </label>
    </div>

    <div>
    <label className=''>

        Crime Commited:
        <input
          type="text" 
          className=''
          placeholder='    Enter your phone no.'
          required
        />
      </label>
    </div>

    <div>
      <label >
        Officer in Charge:
        <input
          className=''
          type="text"
          placeholder='   Enter criminal name'
          required
        />
      </label>
    </div>

    <div>
      <label >
        Officer id:
        <input
          className=''
          type="text"
          placeholder='     Enter criminal name'
          required
        />
      </label>
    </div>


    <button
    type="submit" 
    className=''>
               Submit
    </button>
   </form> 

  

   
    </div>
    
    
    </div>
  )
}

export default Form;

