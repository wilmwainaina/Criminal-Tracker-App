import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Form from './pages/Form';
import Tables from './pages/Tables';
import SideBar from './components/SideBar';
import ParentComponent from './components/ParentComponent'

function App() {
  return (
          <Router>
    
              <div className='App'>
                    <SideBar />
                <Routes>

               <Route path="/" element={<Home />} />
               <Route path="/form" element={<Form />} />
               <Route path="/list" element={<Tables />} />
               <Route path="/parent" element={<ParentComponent />} /> {/* Add a new route */}
               </Routes>
          
        </div>
      
    </Router>
  );
}

export default App;