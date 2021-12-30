import styled from "styled-components";
import { theme } from "styled-tools";
import { Link } from "react-router-dom";
export default function RegisterDone() {
  return (
    <>
      <Wrap>
        <p>식스맨 비대면 극장에 오신것을 환영합니다!</p>
        <p>코로나19로 지친 님에게 좋은 위로가 될 수 있기를 바랍니다.</p>
        <br />
        <br />
        <br />
        <Link to="/login">
          <Button isMini={true}>로그인</Button>
        </Link>
      </Wrap>
    </>
  );
}

const Wrap = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 30vh;
  ${theme("fonts.textH2")} ${theme("neons.textNeonGold")};
`;
// const IdWrap = styled.div`
//   display: flex;
//   flex-direction: column;
//   justify-content: center;
//   margin-bottom: 5rem;
//   ${theme("fonts.textH3")}
//   ${theme("neons.textNeonGold")};
// `;

// const PassWrap = styled.div`
//   display: flex;
//   flex-direction: column;
//   justify-content: center;
//   margin-bottom: 5rem;
//   ${theme("fonts.textH3")}
//   ${theme("neons.textNeonGold")};
// `;

// const PassconWrap = styled.div`
//   display: flex;
//   flex-direction: column;
//   justify-content: center;
//   margin-bottom: 3rem;
//   ${theme("fonts.textH3")}
//   ${theme("neons.textNeonGold")};
// `;

// const Input = styled.input`
//   width: 20rem;
//   border-radius: 2rem;
//   color: white;
//   ${theme("fonts.textH2")} ${theme("neons.boxNeonGold")};
// `;

// const Select = styled.select`
//   width: 10rem;
//   height: 4rem;
//   background-color: black;
//   color: white;
//   font-size: 2rem;
//   text-align: center;
//   border-radius: 2rem;
//   margin-bottom: 5rem;
//   ${theme("fonts.textH2")} ${theme("neons.boxNeonGold")};
// `;

const Button = styled.span`
  cursor: pointer;
  border-bottom: 0.1rem solid ${theme("colors.mainBlack")};
  padding: 2rem 3.5rem;
  color: ${theme("colors.mainWhite")};
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH3")}

  &:hover {
    color: ${theme("colors.mainPoint")};
    border-color: ${theme("colors.mainPoint")};
  }
`;
