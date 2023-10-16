import React from "react";
import { HiHome, HiPlus, HiClipboard } from "react-icons/hi";
import { useLocation } from "react-router-dom"; // Import useLocation from react-router-dom

const iconSize = 40;

const SideBar = () => {
  const location = useLocation(); // Get the current location using useLocation()

  return (
    <div className="container">
      <div className="sidebar">
        <ul>
          <li className={location.pathname === "/" ? "active" : ""}>
            <HiHome size={iconSize} className="" />
            <a href="/">home</a>
          </li>

          <li className={location.pathname === "/form" ? "active" : ""}>
            <HiPlus size={iconSize} className="" />
            <a href="/form">form</a>
          </li>

          <li className={location.pathname === "/tables" ? "active" : ""}>
            <HiClipboard size={iconSize} className="" />
            <a href="/tables">tables</a>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default SideBar;


