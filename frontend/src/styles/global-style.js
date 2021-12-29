import { createGlobalStyle } from "styled-components";
import reset from "styled-reset";
import { theme } from "styled-tools";

export const GlobalStyle = createGlobalStyle`
  ${reset}

  * {
    box-sizing: border-box;
  }

  @font-face {
    font-family: "RobotoSlab";
    font-weight: normal;
    font-style: normal;
    src: url("/fonts/NotoSansKR-Regular.otf") format("opentype");
  }

  @font-face {
    font-family: "NotoSansSerif";
    font-weight: normal;
    font-style: normal;
    src: url("/fonts/NotoSansKR-Light.otf") format("opentype");
  }

  html {
    background-color: ${theme("colors.mainBlack")};
    color: ${theme("colors.mainWhite")};
    font-family: NotoSansKR;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  input, button {
    outline: none; 
    border: none;
    background-color: transparent;                                                                                                                                                                        
  }

  button {
    cursor: pointer;
    display: flex;
    align-items: center;
    background-color: transparent;
  }
`;

export default GlobalStyle;
