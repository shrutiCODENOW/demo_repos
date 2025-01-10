import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { setupServer } from 'msw/node';
import { rest } from 'msw';
import MovieList from './MovieList';
import store from './store';

// Mock Movie API responses
const mockMovies = {
  Search: [
    {
      Title: 'Movie 1',
      Year: '2020',
      imdbID: '1',
      Poster: 'https://via.placeholder.com/150',
    },
    {
      Title: 'Movie 2',
      Year: '2021',
      imdbID: '2',
      Poster: 'https://via.placeholder.com/150',
    },
  ],
  totalResults: '2',
};

const server = setupServer(
  rest.get('https://www.omdbapi.com/', (req, res, ctx) => {
    return res(ctx.json(mockMovies));
  })
);

// Initialize Query Client
const queryClient = new QueryClient();

describe('MovieList Component', () => {
  // Start and stop MSW server
  beforeAll(() => server.listen());
  afterEach(() => server.resetHandlers());
  afterAll(() => server.close());

  const renderMovieList = () =>
    render(
      <Provider store={store}>
        <QueryClientProvider client={queryClient}>
          <MemoryRouter>
            <MovieList />
          </MemoryRouter>
        </QueryClientProvider>
      </Provider>
    );

  it('renders the MovieList component', async () => {
    renderMovieList();

    // Wait for movies to load
    await waitFor(() => expect(screen.getByText(/Movie 1/i)).toBeInTheDocument());

    // Check if movies are rendered
    expect(screen.getByText(/Movie 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Movie 2/i)).toBeInTheDocument();
  });

  it('shows a loading spinner while fetching movies', async () => {
    renderMovieList();

    // Check for the spinner before movies are loaded
    expect(screen.getByText(/Loading/i)).toBeInTheDocument();

    // Wait for movies to load
    await waitFor(() => expect(screen.getByText(/Movie 1/i)).toBeInTheDocument());
  });

  it('displays "No movies found" if no movies match the query', async () => {
    server.use(
      rest.get('https://www.omdbapi.com/', (req, res, ctx) => {
        return res(ctx.json({ Search: [] }));
      })
    );

    renderMovieList();

    // Wait for movies to load
    await waitFor(() => expect(screen.getByText(/No movies found/i)).toBeInTheDocument());
  });

  it('filters movies based on genre', async () => {
    renderMovieList();

    // Wait for movies to load
    await waitFor(() => expect(screen.getByText(/Movie 1/i)).toBeInTheDocument());

    // Simulate selecting a genre (e.g., Action)
    fireEvent.change(screen.getByLabelText(/Genre/i), { target: { value: 'Action' } });

    // Check if no movies are shown for unmatched genres
    expect(screen.getByText(/No movies found/i)).toBeInTheDocument();
  });

  it('navigates to a movie details page when clicked', async () => {
    renderMovieList();

    // Wait for movies to load
    await waitFor(() => expect(screen.getByText(/Movie 1/i)).toBeInTheDocument());

    // Simulate clicking on a movie
    fireEvent.click(screen.getByText(/Movie 1/i));

    // Check if navigation happened (mock routes if needed)
    expect(global.window.location.pathname).toBe('/movie/1');
  });

  it('toggles sorting order on button click', async () => {
    renderMovieList();

    // Wait for movies to load
    await waitFor(() => expect(screen.getByText(/Movie 1/i)).toBeInTheDocument());

    // Simulate clicking the toggle sort order button
    const toggleButton = screen.getByText(/Sort Order/i);
    fireEvent.click(toggleButton);

    // Check if sort order toggled
    expect(screen.getByText(/Sort Order: Descending/i)).toBeInTheDocument();

    fireEvent.click(toggleButton);
    expect(screen.getByText(/Sort Order: Ascending/i)).toBeInTheDocument();
  });
});
