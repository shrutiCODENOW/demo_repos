import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  query: '', // Store search query or random keyword
  page: 1,   // Current page
};

const movieSlice = createSlice({
  name: 'movies',
  initialState,
  reducers: {
    setQuery: (state, action) => {
      state.query = action.payload; // Update query
      state.page = 1; // Reset page to 1 when query changes
    },
    setPage: (state, action) => {
      state.page = action.payload; // Update page
    },
  },
});

export const { setQuery, setPage } = movieSlice.actions;
export default movieSlice.reducer;
