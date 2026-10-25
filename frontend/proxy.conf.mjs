// Dev server proxy: /api -> Flask. Inside Docker the target is the backend service.
export default {
  '/api': {
    target: process.env.API_URL || 'http://localhost:5000',
    secure: false,
    changeOrigin: true,
  },
};
