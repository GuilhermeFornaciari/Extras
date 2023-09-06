using AwesomeDevEvents.API.Entites;
using AwesomeDevEvents.API.Persistence;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;

namespace AwesomeDevEvents.API.Controllers
{
    [Route("api/dev-event")]
    [ApiController]
    public class DevEventController : ControllerBase
    {
        private readonly DevEventDbContext _context;
        public DevEventController(DevEventDbContext context)
        {
            _context = context;
        }
        [HttpGet]
        public IActionResult GetAll() 
        {
            return Ok(_context.DevEvents.Where(d => !d.IsDeleted).ToList());
        }
        [HttpGet("{id}")]
        public IActionResult GetByid(Guid id)
        {
                var devEvent = _context.DevEvents.SingleOrDefault(d => d.Id == id);
            if (devEvent == null) return NotFound();
            return Ok(devEvent);
        }

        [HttpPost]
        public IActionResult Post(DevEvent devEvent)
        {
            _context.DevEvents.Add(devEvent);
            return CreatedAtAction(nameof(GetByid), new { id = devEvent.Id }, devEvent);
        }

        [HttpPut("{id}")]
        public IActionResult Update(Guid id, DevEvent input)
        {
            var devEvent = _context.DevEvents.SingleOrDefault(d => d.Id == id);
            if (devEvent == null) return NotFound();
            devEvent.Update(input.Title,input.Description,input.StartDate, input.EndDate);
            return NoContent();

        }

        [HttpDelete("{id}")]
        public IActionResult GetAll(Guid id)
        {
            var devEvent = _context.DevEvents.SingleOrDefault(d => d.Id == id);
            if (devEvent == null) return NotFound();
            devEvent.Delete();
            return NoContent();



        }
    }
}
