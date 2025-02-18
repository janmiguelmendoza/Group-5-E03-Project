class Job:
    def __init__(self, job_id, title, description, requirements, employer):
        self.job_id = job_id
        self.title = title
        self.description = description
        self.requirements = requirements
        self.employer = employer
        self.applications = []
    
    def save(self, db):
        db.execute('INSERT INTO job (id, title, description, requirements, employer) VALUES (?, ?, ?, ?, ?)',
                   (self.job_id, self.title, self.description, self.requirements, self.employer))
    
    def delete(self, db):
        db.execute('DELETE FROM job WHERE id = ?', (self.job_id,))
    
    def update_job_details(self, db, title, description, requirements):
        db.execute('UPDATE job SET title = ?, description = ?, requirements = ? WHERE id = ?',
                   (title, description, requirements, self.job_id))
    
    def fetch_applications(self, db):
        self.applications = db.fetchall('SELECT * FROM application WHERE job_id = ?', (self.job_id,))
