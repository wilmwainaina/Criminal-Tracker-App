import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Form from './pages/Form';
import List from './pages/List';
import SideBar from './components/SideBar';


function App() {
  return (
          <Router>
    
              <div className='App'>
                    <SideBar />
                <Routes>

               <Route path="/" element={<Home />} />
               <Route path="/form" element={<Form />} />
               <Route path="/list" element={<List />} />
               
               </Routes>
          
        </div>
      
    </Router>
  );
}

export default App;