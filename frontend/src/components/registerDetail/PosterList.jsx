import styled from "styled-components";
import { Poster } from "..";
import {
  poster01,
  poster02,
  poster03,
  poster04,
  poster05,
  poster06,
  poster07,
  poster08,
  poster09,
  poster10,
  poster11,
  poster12,
  poster13,
  poster14,
  poster15,
  poster16,
} from "../../assets/images";

const TEMPPOSTERS = [
  poster01,
  poster02,
  poster03,
  poster04,
  poster05,
  poster06,
  poster07,
  poster08,
  poster09,
  poster10,
  poster11,
  poster12,
  poster13,
  poster14,
  poster15,
  poster16,
];

export default function PosterList() {
  return (
    <Wrapper>
      {TEMPPOSTERS.map((poster, idx) => (
        <Poster key={`poster-${idx}`} imgSrc={poster} />
      ))}
    </Wrapper>
  );
}

const Wrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  width: 95rem;
  row-gap: 5rem;
  column-gap: 4.5rem;
`;
