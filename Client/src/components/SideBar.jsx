import React from "react";
import { HiHome, HiPlus, HiClipboard} from "react-icons/hi";
import { BsGear} from "react-icons/bs";


const iconSize = 40;


const SideBar = () => {
  return (
    
 <div className="conatiner">

  <div className="sidebar">
  <ul className="">
    <li
      className={location.pathname === "/home"}>
        <HiHome  size={iconSize} className=""/>
    <a href="/">home</a>
    </li>
    <li
      className={location.pathname === "/form"}>
        <HiPlus size={iconSize} className=""/>
    <a href="/form">form</a>
    </li>
    <li
      className={location.pathname === "/crimetables"}>
        <HiClipboard size={iconSize} className=""/>
    <a href="/crimetables">tables</a>
    </li>
   
  </ul>
  </div>
 </div>
  );
};

export default SideBar;