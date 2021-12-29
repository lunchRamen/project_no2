import { RecoilRoot } from "recoil";
import { ThemeProvider } from "styled-components";
import Router from "./pages/Router";
import { GlobalStyle } from "./styles/global-style";
import theme from "./styles/theme";

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <RecoilRoot>
        <GlobalStyle />
        <Router />
      </RecoilRoot>
    </ThemeProvider>
  );
};

export default App;
