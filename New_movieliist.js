import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setQuery, setPage } from '../store/movieSlice';
import { useQuery } from '@tanstack/react-query';
import { fetchMovies } from '../api/movieApi';
import Pagination from './Pagination';
import styled from 'styled-components';

// Styled Components
const Container = styled.div`
  padding: 20px;
`;

const MovieGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
`;

const MovieCard = styled.div`
  background: ${(props) => props.theme.cardBg};
  color: ${(props) => props.theme.text};
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;

  img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 5px;
  }
`;

const MovieList = () => {
  const dispatch = useDispatch();
  const query = useSelector((state) => state.movies.query); // Get query from Redux store
  const page = useSelector((state) => state.movies.page);   // Get page from Redux store

  // Keywords for random searches
  const randomKeywords = ['action', 'love', 'war', 'comedy', 'drama', 'horror', 'thriller', 'adventure', 'sci-fi', 'mystery'];

  // Set a random keyword on initial render
  useEffect(() => {
    if (!query) {
      const randomQuery = randomKeywords[Math.floor(Math.random() * randomKeywords.length)];
      dispatch(setQuery(randomQuery)); // Dispatch action to set query in Redux
    }
  }, [dispatch, query, randomKeywords]);

  // React Query for fetching movies
  const { data, isLoading, error } = useQuery({
    queryKey: ['movies', query, page], // Query key
    queryFn: () => fetchMovies(query, page), // Query function
    enabled: !!query, // Only fetch if query is not empty
    keepPreviousData: true, // Cache previous data for smooth transitions
  });

  // Handle page change
  const handlePageChange = (newPage) => {
    dispatch(setPage(newPage)); // Update page in Redux store
  };

  // Loading and error handling
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error fetching movies!</div>;
  if (!data?.Search) return <div>No results found.</div>;

  return (
    <Container>
      <MovieGrid>
        {data.Search.map((movie) => (
          <MovieCard key={movie.imdbID}>
            <img src={movie.Poster} alt={movie.Title} />
            <h3>{movie.Title}</h3>
            <p>{movie.Year}</p>
          </MovieCard>
        ))}
      </MovieGrid>
      <Pagination
        currentPage={page}
        totalPages={Math.ceil(data.totalResults / 10)}
        onPageChange={handlePageChange}
      />
    </Container>
  );
};

export default MovieList;
          
